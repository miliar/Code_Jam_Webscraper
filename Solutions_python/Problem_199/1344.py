
def flip_pancakes(index,pancakes,k):
    if index + k > len(pancakes):
        return pancakes,False
    pancakes_front = pancakes[:index]
    pancakes_back = pancakes[index+k:]
    pancakes_flipped = ""
    for i in range(k):
        if pancakes[index+i] == "+":
            pancakes_flipped += "-"
        else:
            pancakes_flipped += "+"
    return pancakes_front + pancakes_flipped + pancakes_back, True


def main():
    t = input()
    for i in range(1,t+1):
        pancakes,k = raw_input().split(" ")
        k = int(k)

        index = 0
        count = 0
        flipped = True
        while index < len(pancakes):
            if pancakes[index] == "+":
                index += 1
            else:
                pancakes,flipped = flip_pancakes(index,pancakes,k)
                if flipped == False:
                    print("Case #{}: {}".format(i, "IMPOSSIBLE"))
                    break
                else:
                    count += 1
        
        if flipped == True:
            print("Case #{}: {}".format(i, count))

main()