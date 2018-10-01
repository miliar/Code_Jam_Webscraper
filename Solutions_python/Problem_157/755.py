import time
start_time = time.time()

f = open("C-small-attempt2.in", 'r')
#f = open("test.in", 'r')
out = open("Answer.txt", "w")

quat_results = {}

    
results1 = {}
results1["1"] = "1"
results1["i"] = "i"
results1["j"] = "j"
results1["k"] = "k"
results1["-1"] = "-1"
results1["-i"] = "-i"
results1["-j"] = "-j"
results1["-k"] = "-k"

quat_results["1"] = results1

results1 = {}
results1["1"] = "i"
results1["i"] = "-1"
results1["j"] = "k"
results1["k"] = "-j"
results1["-1"] = "-i"
results1["-i"] = "1"
results1["-j"] = "-k"
results1["-k"] = "j"

quat_results["i"] = results1

results1 = {}
results1["1"] = "j"
results1["i"] = "-k"
results1["j"] = "-1"
results1["k"] = "i"
results1["-1"] = "-j"
results1["-i"] = "k"
results1["-j"] = "1"
results1["-k"] = "-i"

quat_results["j"] = results1

results1 = {}
results1["1"] = "k"
results1["i"] = "j"
results1["j"] = "-i"
results1["k"] = "-1"
results1["-1"] = "-k"
results1["-i"] = "-j"
results1["-j"] = "i"
results1["-k"] = "1"

quat_results["k"] = results1


######

results1 = {}
results1["-1"] = "1"
results1["-i"] = "i"
results1["-j"] = "j"
results1["-k"] = "k"
results1["1"] = "-1"
results1["i"] = "-i"
results1["j"] = "-j"
results1["k"] = "-k"

quat_results["-1"] = results1

results1 = {}
results1["-1"] = "i"
results1["-i"] = "-1"
results1["-j"] = "k"
results1["-k"] = "-j"
results1["1"] = "-i"
results1["i"] = "1"
results1["j"] = "-k"
results1["k"] = "j"

quat_results["-i"] = results1

results1 = {}
results1["-1"] = "j"
results1["-i"] = "-k"
results1["-j"] = "-1"
results1["-k"] = "i"
results1["1"] = "-j"
results1["i"] = "k"
results1["j"] = "1"
results1["k"] = "-i"

quat_results["-j"] = results1

results1 = {}
results1["-1"] = "k"
results1["-i"] = "j"
results1["-j"] = "-i"
results1["-k"] = "-1"
results1["1"] = "-k"
results1["i"] = "-j"
results1["j"] = "i"
results1["k"] = "1"

quat_results["-k"] = results1


line_type = -1
X = 0
L = 0
case = 1
answer = 0
k_seen = 0
for line in f:
    if line_type == -1:
        line_type = 0
        continue

    if line_type == 0:
        stuff = line.split(" ")
        L = int(stuff[0])
        X = int(stuff[1])
        line_type = 1
        continue

    line_type = 0
    i_answers = []
    j_answers = []
    k_answers = {}

    line = line.strip("\n")
    string = ""
    for y in range(0, X):
        string += line

    result = "1"
    for index in range(0, L * X - 2):
        result = quat_results[result][string[index]]
        if result == "i":
            i_answers.append(index + 1)

    result = "1"
    for index in range(L*X - 1, 1, -1):
        result = quat_results[string[index]][result]
        if result == "k":
            k_answers[index] = 1

    for index in range(0, len(i_answers)):
        result = "1"
        for y in range(i_answers[index], L*X - 1):
            result = quat_results[result][string[y]]

            if result == "j":
                if (y + 1) in k_answers:
                    answer = 1
            if answer == 1:
                break
        if answer == 1:
            break


                       
    if answer == 1:
        output = "Case #" + str(case) + ": YES\n"
    else:
        output = "Case #" + str(case) + ": NO\n"
    out.write(output)
    case += 1
    answer = 0
    k_seen = 1
        
f.close()
out.close()
print("--- %s seconds ---" % (time.time() - start_time))
