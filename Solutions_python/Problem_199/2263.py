
output = open("output.txt","wt")
with open("input.txt","r") as f:
    cases = int(f.readline())
    for c in range(cases):
        line,flip = (n for n in f.readline().split(" "))
        flip = int(flip)
        line = [n for n in line]
        count = 0
        answer = 0
        case = c + 1
        length = len(line)
        while answer <= length and count <= 2:
            flag = 1
            for i,l in enumerate(line):
                if l == '-':
                    flag = 0
                    # print(i,length - flip,line)
                    if i <= length - flip:
                        answer += 1
                        for inner in range(i,i+flip):
                            if line[inner] == '+':
                                line[inner] = '-'
                            else:
                                line[inner] = '+'
            if flag:
                break
            count += 1
        if flag:
            print("Case #{0}: {1}".format(case,answer),file = output)
        else:
            print("Case #{0}: IMPOSSIBLE".format(case),file = output)
