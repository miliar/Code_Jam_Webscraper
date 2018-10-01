def main():
    T = int(input())
    for case in range(T):
        Smax, s = input().split()
        standing = 0
        additional = 0
        for shyness, sc in enumerate(s):
            c = int(sc)
            if c > 0:
                if shyness > standing:
                    diff = (shyness - standing)
                    additional += diff
                    standing += diff
            standing += c
        print("Case #{}: {}".format(case + 1, additional))

if __name__ == '__main__':
    main()
