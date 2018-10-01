#Problem A - v1
#Steed 2: Cruise Control
#Theo Vickery

def main():
    t = int(input())

    case_list = []
    for case in range(t):
        temp = input()
        d, n = tuple([int(i) for i in temp.split()])
        horse_list = []
        for horse in range(n):
            temp = input()
            k, s = tuple([int(i) for i in temp.split()])
            horse_list.append((k,s))
        case_list.append((d, n, horse_list))

    for case_num in range(t):
        d, n, horse_list = case_list[case_num]

        time = 0

        for horse in horse_list:
            k, s = horse
            time_to_finish = (d-k)/s
            time = max(time, time_to_finish)

        final_speed = d/time

        print("Case #{0}: {1}".format(case_num+1, final_speed))
            
        
main()
