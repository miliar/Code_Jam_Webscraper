T = int(raw_input())

for i in range(T):
    line = raw_input()
    num = line.split(" ")
    S_max = int(num[0])
    digits = num[1]
    shy = [0]*(S_max+1)
    for j in range(S_max+1):
        shy[j] = int(digits[j])
    already_standing_up = 0
    additional_guests = 0
    for j in range(S_max+1):
        additional_guests += max(0, j - already_standing_up)
        shy[j] += max(0, j - already_standing_up)
        already_standing_up += shy[j]

    print("Case #{}: {}".format(i+1, additional_guests))
