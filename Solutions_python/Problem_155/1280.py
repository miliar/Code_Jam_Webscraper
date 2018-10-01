import sys

input = sys.stdin

test = int(input.readline())

for test_num in range(1, test+1):
    min_friends = 0

    max_s, ss_str = input.readline().split(' ')
    max_s = int(max_s)

    current_count = 0
    for needed, count in enumerate(ss_str.rstrip()):
        if needed > current_count:
            min_friends += needed - current_count
            current_count = needed
        current_count += int(count)

    print('Case #{}: {}'.format(test_num, min_friends))
