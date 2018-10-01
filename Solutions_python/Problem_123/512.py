import sys

def solve_small(current_size, motes, fixes_needed):
    if len(motes) == 0:
        return fixes_needed
    if motes[0] < current_size:
        current_size += motes[0]
        return solve_small(current_size, motes[1:], fixes_needed)
    else:
        fixes_needed += 1
        fix1 = 10**7
        if current_size > 1:
            new_motes = [current_size - 1] + motes[:]
            fix1 = solve_small(current_size, new_motes, fixes_needed)
        fix2 = solve_small(current_size, motes[1:], fixes_needed)
        return min(fix1, fix2)

def process_files(in_file, out_file):
    tc_count = in_file.readline()
    for tc_idx in range(0, int(tc_count)):
        A, N = map(int, in_file.readline().strip().split())
        sys.setrecursionlimit(1500)
        motes = list(map(int, in_file.readline().strip().split()))
        motes.sort()
        out_file.write('Case #%d: ' % (tc_idx+1))
        print('Case #%d:' % (tc_idx+1))
        #print(solve_small(A, motes, 0))
        
        
        #print('Case #%d:' % (tc_idx+1))
        
        out_file.write("{0}".format(solve_small(A, motes, 0)))
        out_file.write("\n")
        
if __name__ == '__main__':
    with open('A-small-attempt0.in', 'rb') as in_file:
        with open('output.txt', 'wb') as out_file:
            process_files(in_file, out_file)