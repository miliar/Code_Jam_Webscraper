import sys


def solve(max_shy, audience):
    current_crowd = 0
    num_invite = 0
    for shyness, num_ppl in enumerate(audience):
        if shyness > current_crowd:
            num_invite += int(shyness) - current_crowd
            current_crowd += int(shyness) - current_crowd
        current_crowd += int(num_ppl)
    return num_invite


def test():
    print 'Testing...'
    # Given from problem set
    assert solve('4', '11111') == 0
    assert solve('1', '09') == 1
    assert solve('5', '110011') == 2
    assert solve('0', '1') == 0

    # Other test cases
    assert solve('6', '0000009') == 6
    assert solve('6', '0123456') == 1
    assert solve('6', '0123459') == 1
    print 'Success!'


def main():
    output = []
    with open('input.in') as f:
        lines = f.readlines()
        for i in range(1, len(lines)):
            max_shy, audience = lines[i].rstrip().split(' ')
            output.append(solve(max_shy, audience))

    with open('output.out', 'w') as of:
        content = ['Case #{i}: {ans}'.format(i=(i+1), ans=out)
                   for i, out in enumerate(output)]
        of.write('\n'.join(content))


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'test':
        test()
    else:
        main()
