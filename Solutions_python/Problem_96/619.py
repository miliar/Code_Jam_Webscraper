from sys import argv


def main():
    f = open(argv[1], 'r')
    test_cases = int(f.readline())
    count = 0

    while test_cases:
        count = count + 1
        test_cases = test_cases - 1

        data_line = f.readline().rstrip("\n")
        bits = data_line.split(" ")

        googlers = int(bits[0])
        have_surprises_left = int(bits[1])
        target_score = int(bits[2])
        scores = [int(x) for x in bits[3:]]
    
#4
#3 1 5 15 13 11
#3 0 8 23 22 21
#2 1 1 8 0
#6 2 8 29 20 8 18 18 21

#Case #1: 3
#Case #2: 2
#Case #3: 1
#Case #4: 3

        answers = 0
        for score in scores:
            if score == 0 and target_score > 0:
                continue
            myavg = int(score/3)
            mymod = score % 3

            # if avg is over target, don't bother analyzing
            if myavg >= target_score:
                answers = answers + 1
                continue

            if mymod == 0:
                if have_surprises_left and (myavg+1) >= target_score:
                    answers += 1
                    have_surprises_left -= 1
                continue

            if mymod == 1:
                if (myavg+1) >= target_score:
                    answers += 1
                else:
                    if have_surprises_left and (myavg+1) >= target_score:
                        answers += 1
                        have_surprises_left -= 1
                continue

            if mymod == 2:
                if (myavg+1) >= target_score:
                    answers += 1
                else:
                    if have_surprises_left and (myavg+2) >= target_score:
                        answers += 1
                        have_surprises_left -= 1
                continue

        print "Case #%d: %d" % (count, answers)


if __name__ == "__main__":
  main()
