from decimal import *

def main():
    f = open("B-large.in", "r")
    cases = int(f.readline())
    for i in range(1,cases+1):
        case = list(f.readline().split())        
        
        for x in range(0,3):
            case[x] = Decimal(case[x])
            
        time = Decimal(0)
        production = Decimal(2)
        cookies = Decimal(0)
        
        while (cookies < case[2]):
            time_to_farm = (case[0] - cookies) / production
            time_to_goal = (case[2] - cookies) / production
            time_to_goal_after_farm = case[2] / (production + case[1])
            
            #print(time_to_farm, time_to_goal, time_to_goal_after_farm)
            #input("...")

            if (time_to_goal > time_to_farm + time_to_goal_after_farm):
                #buy farm
                cookies += time_to_farm * production
                time += time_to_farm
                production += case[1]
                cookies -= case[0]
            else:
                #to the end
                cookies += time_to_goal * production
                time += time_to_goal
            
        
        print("Case #" + str(i) + ": " + str(time))
        

if __name__ == "__main__":
    main()