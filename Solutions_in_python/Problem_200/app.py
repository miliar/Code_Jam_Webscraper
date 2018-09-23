def get_y(number):
    y = number
    while not is_tidy(y):
        y -= 1
    return y

def is_tidy(number):
    is_tidy = True
    text = str(number)
    if len(text) > 1:
        digit = int(text[0])
        for character in text[1:]:
            if int(character) < digit:
                is_tidy = False
                break
            digit = int(character)
    return is_tidy

T = int(input())
for x in range(1, T + 1):
    N = int(input())
    y = get_y(N)
    print("Case #{}: {}".format(x, y))
