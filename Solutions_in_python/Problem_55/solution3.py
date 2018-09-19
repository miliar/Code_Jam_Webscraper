def read_set(path):
	s = file(path,"rb").read()
	ss = s.splitlines()
	T = eval(ss[0])
	inps = []
	inps = [(map(long,ss[i].split(" ")),map(long,ss[i + 1].split(" "))) for i in range(1,len(ss),2)]
	return T, inps

def solve_one(inp):
    rounds = inp[0][0]
    capacity = inp[0][1]
    groups = inp[1]

    pointer = 0
    count_round = 0
    money = 0
    money_per_round = [0]
    while ((count_round == 0) or (pointer != 0)) and (count_round < rounds):
#    while (count_round < rounds):
        current_boat = 0
        passangers = 0
        while (current_boat <= capacity) and (passangers <= len(groups)):
            current_boat += groups[pointer]
            pointer = (pointer + 1) % len(groups)
            passangers += 1
        pointer = (pointer - 1) % len(groups)
        current_boat -= groups[pointer]
        
        money += current_boat
        count_round += 1
        money_per_round.append(current_boat)

    if count_round < rounds:
        money = money * (rounds / count_round) + reduce(lambda x,y:x+y,money_per_round[:(rounds % count_round) + 1])
    return money

def solve(path_in, path_out):
    s = read_set(path_in)
    inps = s[1]
    res = [solve_one(x) for x in s[1]]
    solution = ''.join(["Case #" + str(i + 1) + ": " + str(res[i]) + "\n" for i in range(len(res))])
    f = file(path_out,"w")
    f.write(solution)
    f.close()
    return solution
