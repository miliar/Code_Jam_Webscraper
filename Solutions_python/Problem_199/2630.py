INPUT_PATH = r"C:/Users/owner/Desktop/codejam16/2017qual/A-large.in"
OUTPUT_PATH = "A-answer.txt"

CASE = "Case #%d: %s\n"
answers = []
with open(INPUT_PATH, "r") as f:
    for t in range(int(f.readline())):
        question = f.readline()
        if question[-1] == "\n":
            question = question[:-1]
        pancakes, flip_size = question.split()
        pancakes = [c for c in pancakes]
        flip_size = int(flip_size)
        required_flips = 0
        for i in range(len(pancakes) - flip_size + 1):
            if pancakes[i] == "-":
                required_flips += 1
                for j in range(i, i + flip_size):
                    if pancakes[j] == "-":
                        pancakes[j] = "+"
                    elif pancakes[j] == "+":
                        pancakes[j] = "-"
        for i in range(len(pancakes) - flip_size + 1, len(pancakes)):
            if pancakes[i] == "-":
                answers.append("IMPOSSIBLE")
                break
        else:
            answers.append(str(required_flips))
with open(OUTPUT_PATH, "w") as f:
    for i in range(len(answers)):
        print(CASE % (i+1, answers[i]))
        f.write(CASE % (i+1, answers[i]))
