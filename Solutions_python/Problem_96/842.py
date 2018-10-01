def pos(n):
    if n<0:
        return 0
    else:
        return n

def single_case(n, s, p, scores):
    """
    n = number of googlers
    s = number of surprising triplets
    p = target score
    scores = list of total scores
    """
    unsurprising_threshhold = pos(p-1)+pos(p-1)+p
    surprising_threshhold = pos(p-2)+pos(p-2)+p
    unsurprising_count = sum([1 for i in scores if i>=unsurprising_threshhold])
    surprising_count = sum([1 for i in scores if unsurprising_threshhold>i>=surprising_threshhold])
    print unsurprising_count, surprising_count
    return unsurprising_count + min(surprising_count, s)

input_file = open('B-large.in')
output_file = open('dancing_output', 'w')
for i, line in enumerate(input_file.readlines()):
    if i==0:
        continue
    else:
        numbers = map(int, line.split())
        count = single_case(numbers[0], numbers[1], numbers[2], numbers[3:])
        output_file.write('Case #%d: %d\n' % (i, count))
input_file.close()
output_file.close()
