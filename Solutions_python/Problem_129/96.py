#!/usr/bin/env python3

import sys
import logging
import argparse

def solve(N, data):
    logging.debug("debug!")
    logging.debug("Data: %s", data)
    logging.debug("N: %s", N)

    def g(n):
        return n * (n - 1) // 2

    def f(n):
        if n == 0:
            return 0
        return n * N - g(n)


    assert f(0) == 0
    assert f(1) == N
    assert f(2) == N+N-1
    assert f(3) == 3 * N -3

    origins = []
    exits = []
    original_score = 0
    events = []
    for row in data:
        origins.append([row[0], row[2]])
        exits.append([row[1], row[2], row[0]])
        original_score += row[2] * f(row[1] - row[0])
        events.append((row[0], "a", row[2]))
        events.append((row[1], "e", row[2]))

    events.sort()

    logging.debug("original: %s", original_score)

    origins.sort(reverse=True)



    new_score = 0
    stack = []
    logging.debug("events: %s", events)
    for event in events:
        logging.debug("stack: %s", stack)
        if event[1] == "a":
            stack.append([event[0], event[2]])
        else:
            loc = event[0]
            p = event[2]
            while p > 0:
                last = stack.pop()
                q = min(p, last[1])
                p -= q
                new_score += q * f(loc - last[0])
                if q < last[1]:
                    stack.append([last[0], last[1] - q])
    logging.debug("new_score_2: %s", new_score)


    # new_score = 0
    # delta = 0
    # for oi in range(len(origins)):
    #     logging.debug("oi: %s", oi)
    #     p = origins[oi][1]
    #     ei = 0
    #     for ei in range(len(exits)):
    #         if p == 0: break
    #         logging.debug("ei: %s p %s", ei, p)
    #         if exits[ei][0] < origins[oi][0]:
    #             continue
    #         q = min(exits[ei][1], p)
    #         logging.debug("q: %s", q)
    #         logging.debug("exiting at %s from %s",
    #                       exits[ei][0], origins[oi][0])

    #         new_score += q * f(exits[ei][0] - origins[oi][0])
    #         delta -= q * ( f(exits[ei][0] - origins[oi][0])  -
    #                        f(exits[ei][0] - exits[ei][2]))

    #         exits[ei][1] -= q
    #         p -= q

    # origins.reverse()


    assert p == 0
    # logging.debug('delta: %s', delta)



    # while True:
    #     logging.debug("oi %s ei %s", oi, ei)
    #     if oi == len(origins) or ei == len(exits):
    #         break

    #     p =  min(origins[oi][1], exits[ei][1])
    #     logging.debug("%s exiting at %s boarded at %s",
    #                   p, exits[ei][0], origins[oi][0])

    #     new_score += (p) * f(exits[ei][0] - origins[oi][0])
    #     logging.debug("new score... %s", new_score)
    #     if origins[oi][1] < exits[ei][1]:
    #         # more exiting than boarding...
    #         oi += 1
    #         exits[ei][1] -= p
    #     else:
    #         ei += 1
    #         origins[oi][1] -= p
    M = 1000002013
    logging.debug("new score: %s", new_score)
    return (original_score - new_score) % M


def main(inp, output):
    T = int(next(inp))
    for case in range(1,T+1):
        N, M = [int(x) for x in next(inp).split()]
        data = [[int(x) for x in next(inp).split()]
                for ii in range(M)]

        r = solve(N, data)
        s = "Case #%d: %s" % (case, r)
        print(s)
        output.write(s + "\n")
        logging.info(s)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="run code jam problem")
    parser.add_argument("filename", type=str, help="input filename")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="enable verbose logging")

    args = parser.parse_args()
    if args.verbose:
        level=logging.DEBUG
    else:
        level=logging.INFO
    logging.basicConfig(level=level,
                        filename="logfile.txt",
                        filemode="w")
    outfile = args.filename + ".out"

    with open(args.filename) as inp:
        with open(outfile, "w") as outp:
            main(inp, outp)
