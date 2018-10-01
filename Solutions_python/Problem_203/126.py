def _p(Cake):
    for r in Cake:
        print(''.join(r))

def solve(R, C, Cake):
    """ solve the problem """

    #print('init', R, C, Cake)
    counted = set([])


    for i in range(R):
        for j in range(C):
            if Cake[i][j] != '?' and Cake[i][j] not in counted:
                init = Cake[i][j]
                counted.add(init)
                left = j
                right = j
                while True:
                    if left - 1 >= 0 and Cake[i][left-1] == '?':
                        left -= 1
                    else: break
                while True:
                    if right + 1 < C and Cake[i][right+1] == '?':
                        right += 1
                    else: break
                top = i
                bottom = i
                while True:
                    if top - 1 >= 0:
                        check = True
                        for j2 in range(left, right+1):
                            if Cake[top-1][j2] != '?': 
                                check = False
                                break
                        if check == True: top -=1
                        else: break
                    else: break
                while True:
                    if bottom + 1 < R:
                        check = True
                        for j2 in range(left, right+1):
                            if Cake[bottom+1][j2] != '?': 
                                check = False
                                break
                        if check == True: bottom +=1
                        else: break
                    else: break

                for i2 in range(top, bottom+1):
                    for j2 in range(left, right+1):
                        Cake[i2][j2] = init

            #_p(Cake)

    #print(R, C, Cake)


    return Cake


def parse():
    """ parse input """
    R, C = [int(i) for i in input().split()]
    Cake = []
    for i in range(R):
        Cake.append(list(input()))

    return R, C, Cake


def main():
    
    T = int(input())

    # solve
    for t in range(1, T+1):
        params = parse()
        #if t != 100: continue
        result = solve(*params)
        #print('Case #%d: %s' % (t, result))
        print('Case #%d:' % t)
        for r in result:
            print(''.join(r))


if __name__ == '__main__':

    main()
