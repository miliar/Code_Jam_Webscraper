testcase_count = int(input())
for testcase_index in range(testcase_count):
    audience = input().split()[1]
    standing = 0
    guests = 0
    for shyness, shy_people in enumerate(audience):
        while standing < shyness:
            guests += 1
            standing += 1
        standing += int(shy_people)
    print("Case #%d: %d" % (testcase_index + 1, guests))
    
