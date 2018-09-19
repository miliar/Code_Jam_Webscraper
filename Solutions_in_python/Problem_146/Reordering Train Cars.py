import sys
import itertools


def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)


def count(cars):
    print(cars)
    for i in range(len(cars)):
        car = ""
        for c in cars[i]:
            if not car or c != car[-1]:
                car += c
        cars[i] = car
    print(cars)
    # cnt = 0
    # for p in itertools.permutations(cars):
    #     check = set()
    #     pc = None
    #     valid = True
    #     for c in ''.join(p):
    #         if c != pc:
    #             if c in check:
    #                 valid = False
    #                 break
    #             check.add(c)
    #         pc = c
    #     if valid:
    #         cnt += 1
    # print(cnt)
    # return cnt % 1000000007
    in_edge = {}
    out_edge = {}
    cnt = {}
    for car in cars:
        c = car[0]
        if c not in cnt:
            cnt[c] = 0
        check = set()
        check.add(c)
        for i in range(1, len(car)):
            if car[i] != c:
                if c in out_edge or car[i] in in_edge or car[i] in check:
                    return 0
                out_edge[c] = car[i]
                in_edge[car[i]] = c
                c = car[i]
                if c not in cnt:
                    cnt[c] = 0
                check.add(c)
        if c == car[0]:
            if c not in cnt:
                cnt[c] = 0
            cnt[c] += 1
    n = len(cnt)
    print(in_edge, out_edge, cnt)
    c = 1
    check = 0
    graph_cnt = 0
    for v in out_edge:
        if v not in in_edge:
            tc = factorial(cnt[v]) % 1000000007
            del cnt[v]
            tv = v
            while tv in out_edge:
                tc = tc * factorial(cnt[out_edge[tv]]) % 1000000007
                del cnt[out_edge[tv]]
                tv = out_edge[tv]
                check += 1
            graph_cnt += 1
            c = c * tc % 1000000007
    for tc in cnt:
        c = c * factorial(cnt[tc]) % 1000000007
        graph_cnt += 1
    print(c, check, graph_cnt)
    return 0 if check != len(out_edge) else c * factorial(graph_cnt) % 1000000007


def main(in_stream, out_stream):
    t = int(in_stream.readline())
    for tc in range(t):
        print(tc)
        n = int(in_stream.readline())
        out_stream.write("Case #%d: %d\n" % (tc + 1, count(list(in_stream.readline().strip().split(' ')))))


if __name__ == '__main__':
    # main(sys.stdin, sys.stdout)
    main(open("B-large.in", "r"), open("B-large-output.txt", "w"))