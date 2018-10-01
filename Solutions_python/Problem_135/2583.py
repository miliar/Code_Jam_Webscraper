with open("input.txt") as f:
    content = f.readlines()
    
number_of_testcases = int(content[0])
#print("Number of test cases:", number_of_testcases)

f = open('output.txt', 'w')


for x in range(0, number_of_testcases):
    first_answer = int(content[x*10+1])
    #print("First answer: ", first_answer)
    second_answer = int(content[x*10+6])
    #print("Second answer: ", second_answer)
    
    first_playfield = [content[x*10+2],content[x*10+3],content[x*10+4],content[x*10+5]]
    second_playfield = [content[x*10+7],content[x*10+8],content[x*10+9],content[x*10+10]]
    #print("first_playfield", first_playfield)
    #print("second_playfield", second_playfield)
    
    selected_row_1 = first_playfield[first_answer - 1].split()
    selected_row_2 = second_playfield[second_answer - 1].split()
    #print("selected_row_1", selected_row_1)
    #print("selected_row_2", selected_row_2)
    solutions = []
    for y in range (0, 4):
        for z in range (0, 4):
            if int(selected_row_1[y]) == int(selected_row_2[z]):
                solutions.append(int(selected_row_1[y]))
            
    solutions = list(set(solutions))
    if (len(solutions) == 1):
        f.write("Case #" + str(x+1) + ": " + str(solutions[0]) + "\n")
    if (len(solutions) > 1):
        f.write("Case #" + str(x+1) + ": Bad magician!\n")
    if (len(solutions) < 1):
        f.write("Case #" + str(x+1) + ": Volunteer cheated!\n")
        
f.close()