#!/usr/bin/python3

t = int(input())

for test_num in range(t):
    shy_max, levels = input().split()
    shy_max = int(shy_max)
    invitees = 0
    people = 0
    for s_level in range(shy_max + 1):
        shy_people = int(levels[s_level])
        if people < s_level and shy_people > 0:
            invitees += s_level - people
            people = s_level
        people += shy_people

    print('Case #{}: {}'.format(test_num + 1, invitees))
