## Ran using python 3.5.
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
import collections
import itertools
import operator

def formatted(answer, case_num):
    return 'Case #{}: {} {}'.format(case_num,
                                    int(answer[0]),
                                    int(answer[1]))

def answer(line):
    Span = collections.namedtuple('Span', ['left_most_stall', 'right_most_stall', 'length'])
    line_list = line.split(' ')
    num_stalls = int(line_list[0])
    num_people = int(line_list[1])
    ## When all stalls are taken:
    if num_people == num_stalls:
        return (0, 0)
    ## When only one person is using a stall:
    if num_people == 1:
        if num_stalls % 2 == 0:
            ## Return (MAX, MIN)
            return (num_stalls / 2, (num_stalls / 2) - 1)
        else:
            return ((num_stalls - 1) / 2, (num_stalls - 1) / 2)

    ## TODO: If the number of people is over 50% of the number of
    ## stalls, the answer will always be 0, 0.

    ## All other scenarios:
    smallest_num = num_stalls
    last_lengths = (0, 0)
    stall_segment_queue = {}
    stall_segment_queue[num_stalls] = [Span(1, num_stalls, num_stalls)]
    for _ in itertools.repeat(None, num_people):
        largest_lengths = max(stall_segment_queue.keys())
        temp_list = stall_segment_queue[largest_lengths]

        '''
        found_all_longest = False
        while not found_all_longest:
            try:
                span_2 = stall_segment_queue.popleft()
                ##print(temp_list)
                if temp_list[0].length != span_2.length:
                    stall_segment_queue.appendleft(span_2)
                    found_all_longest = True
                else:
                    temp_list.append(span_2)
            except IndexError:
                ##this means that there is only one set of stalls left.
                found_all_longest = True
        '''

        temp_list = sorted(temp_list, key=operator.attrgetter('left_most_stall'), reverse=True)
        temp_span = temp_list.pop()
        if smallest_num >= temp_span.length:
            smallest_num = temp_span.length
        else:
            print('ERROR on stalls={} people={}'.format(num_stalls, num_people))
        if len(temp_list) > 0:
            stall_segment_queue[largest_lengths] = temp_list
        else:
            del stall_segment_queue[largest_lengths]
        '''
        temp_len = len(temp_list)
        for _ in itertools.repeat(None, temp_len - 1):
            stall_segment_queue.appendleft(temp_list.pop())
        temp_span = temp_list[0]
        '''
        ## If temp_span.length is even, current_stall = divide by two.
        ## If temp_span.length is odd, current_stall = add one and divide by two.
        ## New left span starts at temp_span.left_most_stall.
        ## New left span ends at current_stall.
        ## New right span starts at current_stall.
        ## New right span ends at temp_span.right_most_stall.
        temp_center = temp_span.left_most_stall + temp_span.right_most_stall
        if temp_center % 2 == 0:
            current_stall = (temp_center) / 2
        else:
            current_stall = (temp_center - 1) / 2
        last_lengths = (current_stall - temp_span.left_most_stall,
                        temp_span.right_most_stall - current_stall)
        temp_left_span = Span(temp_span.left_most_stall,
                              current_stall - 1,
                              current_stall - temp_span.left_most_stall)
        temp_right_span = Span(current_stall + 1,
                               temp_span.right_most_stall,
                               temp_span.right_most_stall - current_stall)
        reappend_list = []
        if temp_left_span.right_most_stall >= temp_left_span.left_most_stall:
            reappend_list.append(temp_left_span)
        if temp_right_span.right_most_stall >= temp_right_span.left_most_stall:
            reappend_list.append(temp_right_span)
        for temp_span in reappend_list:
            try:
                stall_segment_queue[temp_span.length].append(temp_span)
            except KeyError:
                stall_segment_queue[temp_span.length] = [temp_span]
        '''
        for temp_span in reversed(sorted(reappend_list, key=operator.attrgetter('length'))):
            stall_segment_queue.append(temp_span)
        '''
    return list(reversed(sorted(last_lengths)))




t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    line = input()
    print(formatted(answer(line), i))



##print(formatted(answer('9 6'), 1))



"""
slots   people      Solution
3       2           0 0
x000x
x0x0x
xxx0x

4       2           1 0
x0000x
x0x00x
x0xx0x

5       2           1 0
x00000x
x00x00x
xx0x00x

5       4           0 0
x00000x
x00x00x
xx0x00x
xx0xx0x
xxxxx0x

6       2           1 1
x000000x
x00x000x
x00x0x0x

7       4           0 0
x0000000x
x000x000x
x0x0x000x
x0x0x0x0x
xxx0x0x0x

8       
x00000000x
x000x0000x
x000x0x00x
x0x0x0x00x
x0x0x0xx0x

9       6
x000000000x
x0000x0000x
x0x00x0000x
x0x00x0x00x
x0xx0x0x00x
x0xx0x0xx0x
xxxx0x0xx0x

10      
x0000000000x
x0000x00000x
x0000x00x00x
x0x00x00x00x
x0xx0x00x00x
x0xx0xx0x00x
x0xx0xx0xx0x

12
x000000000000x
x00000x000000x
x00000x00x000x
x00x00x00x000x
x00x00x00x0x0x
xx0x00x00x0x0x
xx0xx0x00x0x0x
xx0xx0xx0x0x0x

20      10          1 0
x00000000000000000000x
x000000000x0000000000x
x000000000x0000x00000x
x0000x0000x0000x00000x
x0000x0000x0000x00x00x
x0x00x0000x0000x00x00x
x0x00x0x00x0000x00x00x
x0x00x0x00x0x00x00x00x
x0xx0x0x00x0x00x00x00x
x0xx0x0xx0x0x00x00x00x
x0xx0x0xx0x0xx0x00x00x

x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000x
0000000000000000000000000000000000000000000000000x00000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000x000000000000000000000000x0000000000000000000000000
000000000000000000000000x000000000000000000000000x000000000000000000000000x0000000000000000000000000
000000000000000000000000x000000000000000000000000x000000000000000000000000x000000000000x000000000000
"""
