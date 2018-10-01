import sys


def trick(first_row, first_cards, second_row, second_cards):
    common = first_cards[first_row].intersection(second_cards[second_row])
    return common


def read_row_cards():
    row = int(sys.stdin.readline().strip())
    cards = {}
    for i in range(1, 5):
        cards[i] = set(sys.stdin.readline().split())
    return row, cards


def format_answer(index, answer):
    if len(answer) > 1:
        message = "Bad magician!"
    elif len(answer) == 0:
        message = "Volunteer cheated!"
    else:
        message = answer.pop()
    output_line = "Case #%d: %s" % (index + 1, message)
    return output_line


def display_results(answers):
    output_lines = []
    for index in range(len(answers)):
        output_line = format_answer(index, answers[index])
        output_lines.append(output_line)
    output = "\n".join(output_lines)
    with open("magic_out.txt", "w") as f:
        print("%s" % output, file=f)


def main():
    line = sys.stdin.readline()
    test_cases = int(line.strip())
    answers = []
    for _ in range(test_cases):
        first_row, first_cards = read_row_cards()
        second_row, second_cards = read_row_cards()
        answer = trick(first_row, first_cards, second_row, second_cards)
        answers.append(answer)
    display_results(answers)


if __name__ == "__main__":
    main()
