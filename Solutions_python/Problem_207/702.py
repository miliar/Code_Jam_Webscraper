def solve(N, R, Y, B):
    num_color = sorted([('R', R), ('Y', Y), ('B', B)], key=lambda color: color[1])
    if num_color[2][1] - num_color[1][1] > num_color[0][1]:
        return ''
    else:
        if num_color[2][0] == 'R':
            answer = 'BRYR' * (num_color[2][1] - num_color[1][1])
        elif num_color[2][0] == 'Y':
            answer = 'BYRY' * (num_color[2][1] - num_color[1][1])
        else:
            answer = 'BRBY' * (num_color[2][1] - num_color[1][1])
        # print(answer)

        if len(answer) > 0 and answer[-1] == 'B':
            answer += 'RBY' * (num_color[0][1] - (num_color[2][1] - num_color[1][1]))
        else:
            answer += 'BRY' * (num_color[0][1] - (num_color[2][1] - num_color[1][1]))
        # print(answer)

        if len(answer) > 0 and (answer[-1] == num_color[2][0] or num_color[1][0] == 'B'):
            answer += (num_color[1][0] + num_color[2][0]) * (num_color[1][1] - num_color[0][1])
        else:
            answer += (num_color[2][0] + num_color[1][0]) * (num_color[1][1] - num_color[0][1])

    return answer

T = int(input())
for t in range(T):
    N, R, O, Y, G, B, V = [int(x) for x in input().split()]

    placements = solve(N, R, Y, B)

    if len(placements) == N:
        for i in range(N):
            if placements[i] == placements[(i+1) % N] or placements[i] == placements[i-1]:
                print('XXX')
        print("Case #%d: %s" % (t+1, placements))
    else:
        print("Case #%d: IMPOSSIBLE" % (t + 1))