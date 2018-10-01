
num_tests = int(input())

for foo in range(1, num_tests+1):
    ans1 = int(input())
    cases = []
    for i in range(0, 4):
        cases.append(input().split(' '))
    ans2 = int(input())
    cases2 = []
    for i in range(0, 4):
        cases2.append(input().split(' '))

    matching = [a for a in cases[ans1-1] if a in cases2[ans2-1]]
    num_matching = len(matching)

    if num_matching == 1:
        print("Case #"+str(foo)+": "+str(matching[0]))
    elif num_matching > 1:
        print("Case #"+str(foo)+": Bad Magician!")
    else:
        print("Case #"+str(foo)+": Volunteer cheated!")


