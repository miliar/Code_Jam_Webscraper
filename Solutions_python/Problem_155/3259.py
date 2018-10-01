def main():
    T = int(raw_input())
    for case in range(0, T):
        line = raw_input()
        (Sm, ppl) = line.split()
        Sm = int(Sm)
        ppl = [int(char) for char in ppl]
        clapped = 0
        invited = 0
        for i in range(0, Sm+1):
            if (ppl[i] > 0 and clapped < i):
                invited += (i - clapped)
                clapped = i
            clapped += ppl[i]
        print "Case #%d: %d" % (case+1, invited)

if __name__ == "__main__":
    main()
