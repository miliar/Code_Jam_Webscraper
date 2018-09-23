from contestio import GoogleCodeJam


def main(ln):
    ln, width = ln.split()
    width = int(width)
    OTHER = {'+': '-', '-': '+'}

    flips = 0
    ln = list(ln)
    for i in range(len(ln) - width + 1):
        if ln[i] == '-':
            ln[i:i+width] = map(OTHER.get, ln[i:i+width])
            flips += 1

    if ln.count('-') == 0:
        return flips


if __name__ == '__main__':
    GoogleCodeJam().set(main).run()
