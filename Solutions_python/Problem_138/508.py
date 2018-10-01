from collections import deque

def war(naomi, ken):
    naomi = sorted(naomi, reverse=True)
    ken = deque(sorted(ken, reverse=True))
    wins = 0
    for block in naomi:
        if block > ken[0]:
            wins += 1
            ken.pop()
        else:
            ken.popleft()
    return wins

def deceit(naomi, ken):
    naomi = sorted(naomi)
    ken = deque(sorted(ken))
    wins = 0
    for block in naomi:
        if block > ken[0]:
            wins += 1
            ken.popleft()
        else:
            ken.pop()

    return wins

def main():
    num_cases = int(input())
    for case in range(1, num_cases + 1):
        num_blocks = int(input())
        naomi = list(map(float, input().split()))
        ken = list(map(float, input().split()))

        war_wins = war(naomi, ken)
        deceit_wins = deceit(naomi, ken)
        
        print("Case #{}: {} {}".format(case, deceit_wins, war_wins))

if __name__ == '__main__':
    main()
