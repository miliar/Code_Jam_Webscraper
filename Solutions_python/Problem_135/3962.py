def main():
    t = int(raw_input())

    for i in xrange(t):
        ans = "Case #%d: " % (i+1)
        ans += "%s"
        answer1 = int(raw_input()) - 1
        arrang1 = [map(int,raw_input().split()) for j in range(4)]

        answer2 = int(raw_input()) - 1
        arrang2 = [map(int,raw_input().split()) for j in range(4)]

        once = False
        card = -1
        bad = False
        for opt in arrang1[answer1]:
            if opt in arrang2[answer2] and not once:
                card = str(opt)
                once = True
            elif opt in arrang2[answer2] and once:
                print ans % "Bad magician!"
                bad = True
                break

        if bad:
            continue

        if not once:
            print ans % "Volunteer cheated!"
        else:
            print ans % card


if __name__ == '__main__':
    main()
