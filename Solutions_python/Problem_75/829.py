
from fileinput import input


def run_case(combinations, oppositions, string):
    result = []

    for char in string:
        result.append(char)

        if len(result) >= 2:
            last2 = sorted(result[-2:])

            try:
                elem = combinations[str(last2)]
                result = result[:-2] + list(elem)
            except KeyError:
                last = result[-1]
                for elem in result[:-1]:
                    key, val = sorted([last, elem])

                    try:
                        if val in oppositions[key]:
                            result = []
                    except KeyError:
                        pass

    return result


if __name__ == '__main__':
    first = True
    num = 0
    for line in input():
        if first:
            first = False
        else:
            num += 1
            tokens = line.split()

            combinations = {}
            oppositions = {}

            tok_iter = iter(tokens)

            C = int(tok_iter.next())
            for i in range(C):
                combination = tok_iter.next()
                key = str(sorted(combination[:2]))
                result = combination[2]
                combinations[key] = result

            D = int(tok_iter.next())
            for i in range(D):
                key, val = sorted(tok_iter.next())
                if key not in oppositions:
                    oppositions[key] = set()

                oppositions[key].add(val)

            N = int(tok_iter.next())

            string = tok_iter.next()

            result = run_case(combinations, oppositions, string)
            print "Case #%s: [%s]" % (num, ', '.join(result))
        