

def solve(num_stalls, people):
    if num_stalls * 2 < people * 3:
        return 0, 0

    while people > 1:
        if num_stalls % 2 == 1:
            num_stalls = (num_stalls - 1)/2
            people = people / 2

        elif num_stalls % 2 == 0:
            people -= 1
            if people > 1:
                if people % 2 == 1:
                    people = (people+1)/2
                    num_stalls = num_stalls / 2
                else:
                    people = people / 2
                    num_stalls = (num_stalls-1) / 2
            else:
                num_stalls /= 2

    return (num_stalls)/2, (num_stalls-1)/2


if __name__ == '__main__':
    #with file('bad.in') as f:
    with file('C-large.in') as f:
        _data = f.readline()
        _data = f.readline()
        i = 1
        while _data:
            stalls, people = map(int, _data.strip().split(' '))
            mx, mi = solve(stalls, people)
            print("Case #{x}: {mx} {mi}".format(x=i, mx=mx, mi=mi))
            _data = f.readline()
            i += 1
