
num_tests = int(input())
for test in range(1, num_tests + 1):
    inputs = input().split(' ')
    n, k = int(inputs[0]), int(inputs[1])
    splits = {n: 1}
    i = 0
    while i < k:
        # if i % 1000 == 0:
        #     print('On i={}/{}'.format(i, k))
        best = max(splits.keys())
        best_count = splits[best]
        del splits[best]
        left = best // 2
        right = best - left - 1
        if left > 0:
            if left in splits:
                splits[left] += best_count
            else:
                splits[left] = best_count
        if right > 0:
            if right in splits:
                splits[right] += best_count
            else:
                splits[right] = best_count
        i += best_count

    print('Case #{}: {} {}'.format(test, max(left, right), min(left, right)))
