
def solve(farmcost, farmyield, target):
    cps = 2.0
    time = 0.0
    cookies = 0.0
    targettime = time + (target - cookies) / cps
    while True:
        newtargettime = time + (target - cookies) / cps
        if newtargettime > targettime:
            return targettime
        targettime = newtargettime
        farmtime = (farmcost - cookies) / cps
        time += farmtime
        cps += farmyield

def main():
    numcases = int(input())
    for i in range(numcases):
        farmcost, farmyield, target = map(float, input().split())
        print("Case #{}: {}".format(i+1, solve(farmcost, farmyield, target)))

if __name__ == "__main__":
    main()

