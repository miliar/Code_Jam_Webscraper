# def solve(health, speed, distance, start, end, current_health = 0 , current_speed = 0, current_time = 0.0, first = True):
#     if first:
#         return solve(health, speed, distance, start + 1, end, health[start] - distance[start][start+1], speed[start],
#                      distance[start][start+1] / speed[start], False)
#     elif start == end:
#         return current_time
#     else:
#         change = solve(health, speed, distance, start + 1, end, health[start] - distance[start][start+1], speed[start],
#                      current_time + distance[start][start+1] / speed[start], False)
#         if current_health >= distance[start][start+1]:
#             keep = solve(health, speed, distance, start + 1, end, current_health - distance[start][start+1], current_speed,
#                         current_time + distance[start][start+1] / current_speed, False)
#             return min(keep, change)
#         else:
#             return change

def solve(health, speed, distance, start, end):
    acc_distance = [0]
    print(speed)
    for i in range(end):
        acc_distance.append(acc_distance[-1] + distance[i][i+1])
    print(acc_distance)
    current = []
    time = 0.0
    times = [0.0]
    for i in range(start, end):
        current.append((health[i], speed[i], i))
        new = []
        current_distance = distance[i][i + 1]
        min_time = None
        for current_health, current_speed, current_start in current:
            if current_health - current_distance >= 0:
                new.append((current_health - current_distance, current_speed, current_start))

                temp = times[current_start] + (acc_distance[i + 1] - acc_distance[current_start]) / current_speed
                print("\n**")
                print(current_health, current_speed, current_start)
                print((acc_distance[i + 1] - acc_distance[current_start]))
                print(times[current_start])
                print(temp)
                print("**\n")
                if min_time is None:
                    min_time = temp
                else:
                    min_time = min(temp, min_time)
        current = new
        print(current)
        times.append(min_time)
        print(times)
    print()
    print()
    return times[-1]


def main():
    input_file_name = 'C-input.in'
    output_file_name = 'C-output.out'
    with open(input_file_name) as fin:
        with open(output_file_name, 'w') as fout:
            t = int(fin.readline())
            for tc in range(t):
                n, q = tuple(map(int, fin.readline().split()))
                health = []
                speed = []
                distance = []
                for i in range(n):
                    e, s = tuple(map(int, fin.readline().split()))
                    health.append(e)
                    speed.append(s)

                for i in range(n):
                    distance.append(list(map(int, fin.readline().split())))
                answer = "Case #%d: " % (tc + 1)
                for i in range(q):
                    start, end = list(map(int, fin.readline().split()))
                    answer += str(solve(health, speed, distance, start - 1, end - 1))
                    fout.write(answer+'\n')
main()