def solve(A_C, A_J, activities):
    '''
    1. C 남은 시간, J 남은 시간 구하기
    2. 어쩔 수 없는 교대 횟수(=J와 C 사이 횟수) 세기
    3. J와 J, C와 C 사이 시간을 각각 오름차순 정렬
    :param A_C: 
    :param A_J: 
    :param activities: 
    :return: 
    '''
    remains = {'C': 720 - sum([activity[1] - activity[0] for activity in activities['J']]), 'J': 720 - sum([activity[1] - activity[0] for activity in activities['C']])}
    activity_order = [activity + ['C'] for activity in activities['J']] + [activity + ['J'] for activity in activities['C']]
    activity_order.sort(key=lambda activity: activity[1])

    num_exchanges = 0
    candidates = {'C': [], 'J': []}
    for i in range(A_C + A_J - 1):
        if activity_order[i][2] != activity_order[i+1][2]:
            num_exchanges += 1
        else:
            candidates[activity_order[i][2]].append(activity_order[i+1][0] - activity_order[i][1])
    if activity_order[A_C + A_J - 1][2] != activity_order[0][2]:
        num_exchanges += 1
    else:
        candidates[activity_order[A_C + A_J - 1][2]].append(1440 - activity_order[A_C + A_J - 1][1] + activity_order[0][0])

    candidates['C'].sort()
    candidates['J'].sort()

    # print(remains, activity_order, candidates)

    for i in range(len(candidates['C'])):
        if remains['C'] >= candidates['C'][i]:
            remains['C'] -= candidates['C'][i]
        else:
            num_exchanges += 2 * (len(candidates['C']) - i)
            break
    for i in range(len(candidates['J'])):
        if remains['J'] >= candidates['J'][i]:
            remains['J'] -= candidates['J'][i]
        else:
            num_exchanges += 2 * (len(candidates['J']) - i)
            break

    return num_exchanges

T = int(input())
for t in range(T):
    A_C, A_J = [int(x) for x in input().split()]
    activities = {'C': [], 'J': []}
    for ac in range(A_C):
        activities['C'].append([int(x) for x in input().split()])
    activities['C'].sort(key=lambda time: time[0])
    for aj in range(A_J):
        activities['J'].append([int(x) for x in input().split()])
    activities['J'].sort(key=lambda time: time[0])

    # print(A_C, A_J, activities)
    min_num_exchanges = solve(A_C, A_J, activities)

    print("Case #%d: %d" % (t + 1, min_num_exchanges))