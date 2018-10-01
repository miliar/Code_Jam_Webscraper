import sys


def compute_flips(A, B, K):
    flips = 0
    for i in range(A):
        for j in range(B):
            if i & j < K:
                flips += 1
    return flips


def read_test_case():
    A, B, K = sys.stdin.readline().split()
    A, B, K = int(A), int(B), int(K)
    return A, B, K


def format_answer(index, answer):
    if answer > -1:
        return "Case #%d: %d" % (index + 1, answer)
    else:
        return "Case #%d: Fegla Won" % (index + 1,)


def display_results(answers):
    output_lines = []
    for index in range(len(answers)):
        output_line = format_answer(index, answers[index])
        output_lines.append(output_line)
    output = "\n".join(output_lines)
    with open("lotery_out.txt", "w") as f:
        print("%s" % output, file=f)


def main():
    line = sys.stdin.readline()
    test_cases = int(line.strip())
    answers = []
    for _ in range(test_cases):
        A, B, K = read_test_case()
        flips = compute_flips(A, B, K)
        # print(flips)
        answers.append(flips)
    display_results(answers)


if __name__ == "__main__":
    main()
