import fileinput

def good_dancers(totals, surprising, minpoints):
    result = 0
    for total_str in totals:
        total = int(total_str)
        if total/3 >= minpoints:
            result += 1
        else:
            rest = total - minpoints
            if rest > 0:
                second = rest // 2
                if abs(minpoints-second) < 2:
                    result += 1
                elif abs(minpoints-second) == 2:
                    if surprising > 0:
                        surprising -= 1
                        result += 1
    return result

def main():
    for line in fileinput.input():
        if fileinput.isfirstline():
            continue
        line = line.split()
        result = good_dancers(line[3:], int(line[1]), int(line[2]))
        print("Case #{}: {}".format(fileinput.lineno()-1, result))

if __name__ == '__main__':
    main()
