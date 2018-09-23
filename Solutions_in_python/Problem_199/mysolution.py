
def flipPancakes(pancakes):
    leftPancake = 0
    flips_made = 0
    
    while (leftPancake < (len(pancakes) - k + 1)):
        if (pancakes[leftPancake] == "-"):
            for j in range(leftPancake, leftPancake + k):
                if (pancakes[j] == "-"):
                    pancakes[j] = "+"
                else:
                    pancakes[j] = "-"

            flips_made += 1
        leftPancake += 1   
    
    return flips_made

num_of_loops = int(input())

for i in range(num_of_loops):
    line = input().split(" ")
    pancakes = line[0]
    k = int(line[1])
    pancakes = list(pancakes)
    

    flips_made = flipPancakes(pancakes)

    happy = True
    for pancake in pancakes:
        if (pancake == "-"):
            happy = False
    caseSolution = "" 
    if (happy):
        caseSolution = str(flips_made)
    else:
        caseSolution = ("IMPOSSIBLE")

    print("Case #"+str(i+1)+": " + caseSolution)


