"""
Magicka
Code Jam 2011
"""
import sys

class Magicka(object):
    def __init__(self, combines, opposes):
        self.combines = combines
        self.opposes = opposes
    
    def combine_elements(self, e1, e2):
        for c in self.combines:
            if (c[0] == e1 and c[1] == e2) or (c[0] == e2 and c[1] == e1):
                return c[2]
        return None

    def clear_oppose(self, output):
        e1 = output[-1]
        for op in self.opposes:
            if (op[0] == e1 and op[1] in output) or (op[1] == e1 and op[0] in output):
                # opposed elements exist
                del output[:]

    def compute(self, elements):
        output = [elements[0]]
        for i in range(1, len(elements)):
            if not output:
                output.append(elements[i])
                continue
            c = self.combine_elements(elements[i], output[-1])
            if c:
                output[-1] = c
            else:
                output.append(elements[i])
                self.clear_oppose(output)
        return output

def main():
    num_tests = int(sys.stdin.readline())
    for t in range(1, num_tests + 1):
        line = sys.stdin.readline().split()

        n_combines = int(line.pop(0))
        combines = line[:n_combines]
        del line[:n_combines]

        n_opposes = int(line.pop(0))
        opposes = line[:n_opposes]
        del line[:n_opposes]
        elements = line[-1]

        m = Magicka(combines, opposes)

        result = m.compute(elements)
        result = "".join(result)
        sys.stdout.write("Case #%d: " % t)
        sys.stdout.write("[")
        sys.stdout.write(", ".join(result))
        sys.stdout.write("]")
        sys.stdout.write("\n")

if __name__ == '__main__':
    main()
