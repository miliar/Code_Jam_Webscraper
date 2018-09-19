def main():
    t = int(input())
    outfile = open("output.txt","w")
    for i in range(t):
        rate = 2
        inputs = input().split()
        cost = float(inputs[0])
        rateInc = float(inputs[1])
        goal = float(inputs[2])
        flag = True
        possAnswer = goal/rate
        seconds = cost/rate
        rate += rateInc
        while flag:
            timeTilGoal = goal/rate
            timeTilFarm = cost/rate
            seconds += timeTilGoal
            if possAnswer < seconds:
                flag = False
            else:
                possAnswer = seconds
                seconds = seconds - timeTilGoal + timeTilFarm
                rate += rateInc
        q = str(i+1)
        answer = '%.7f' % possAnswer
        outfile.write("Case #"+q+": "+answer+"\n")

main()
