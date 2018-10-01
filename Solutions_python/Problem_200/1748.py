def main():
    T = int(input())

    for case in range(1, T+1):
        N = input().strip()
        prefix = get_tidy_prefix(N)
        if prefix == N:
            suffix = ''
        else:
            suffix = '9'*(len(N) - len(prefix))
            while len(prefix) > 1 and prefix[-1] == prefix[-2]:
                prefix = prefix[:-1]
                suffix += '9'
            prefix = str(int(prefix) - 1)
            
        print('Case #{}: {}'.format(case, int(prefix + suffix)))

def get_tidy_prefix(number):
    # number should be a string
    size = 1  # single digit is always nondecreasing
    while size < len(number) and number[size-1] <= number[size]:
        size += 1
    return number[:size]
        
if __name__ == '__main__':
    main()


    
