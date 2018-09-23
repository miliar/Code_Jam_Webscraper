from sys import argv

infn = argv[1]
outfn = argv[2]

with open(infn) as f:
    num_examples = int(f.readline().strip())
    Ns = [int(line.strip()) for line in f.readlines()]

def is_tidy(N):
    N_as_str = str(N)
    biggest_digit_seen = N_as_str[0]
    for digit in N_as_str:
        if digit < biggest_digit_seen:
            return False
        if digit > biggest_digit_seen:
            biggest_digit_seen = digit
    return True

def get_biggest_tidy(num_digits):
    return int('9'*num_digits)

def get_smallest_tidy(num_digits, min_digit=1):
    return int(str(min_digit)*num_digits)

#def smallest_uniform_tidy(value):
#    return int(str(value)*len(N))

def find_closest_smaller_tidy(N, min_digit=1):
    if N < 10:
        return N
    elif is_tidy(N) and all([int(d)>=min_digit for d in str(N)]):
        return N
    if N < get_smallest_tidy(len(str(N)), min_digit):
        return get_biggest_tidy(len(str(N))-1)

    T = ""
    highest_digit_seen = 1
    for place, digit in enumerate(str(N)):
        new_digit = None
        for v in range(highest_digit_seen,10):
            if int( T[:place] + (str(v)*len(str(N)[place:])) ) < N:
                new_digit = str(v)
                highest_digit_seen = int(new_digit)
        T += new_digit

    return int(T)

num_processed = 0
with open(outfn, 'w') as outf:
    for i, N in enumerate(Ns, start=1):
        outf.write("Case #{}: {}\n".format(str(i), str(find_closest_smaller_tidy(N))))
        num_processed += 1
        print(str(num_processed))
assert num_processed == num_examples
