# Rob Record 2012
# Fair and Square

from math import sqrt, modf

def is_palindrome(to_eval):
    return str(to_eval) == str(to_eval)[::-1]

def top_square(bottom, top):
    while top >= bottom:
        if modf(sqrt(top))[0] == 0:
            return top
        else:
            top -= 1

    
def bottom_square(bottom, top):
    while bottom <= top:
        if modf(sqrt(bottom))[0] == 0:
            return bottom
        else:
            bottom += 1

fh_in = open('C-small-attempt0.in')
fh_out = open('C-small-attempt0.out', 'w')
iterations = int(fh_in.readline())
print iterations
for i in range(iterations):
    rng = fh_in.readline()
    rng = rng.rstrip("\n")
    rng = rng.split(" ")
    
    bottom = int(rng[0])
    top = int(rng[1])

    new_bottom = bottom_square(bottom, top)
    new_top = top_square(bottom, top)

    print new_bottom, new_top
    possible_fairs = [j for j in range(int(sqrt(new_bottom)), int(sqrt(new_top)) + 1) if is_palindrome(j)]
    final_fairs = [x for x in possible_fairs if is_palindrome(x*x)]
    print final_fairs

    fh_out.write("Case #%d: %d \n" % (i + 1, len(final_fairs)))

fh_in.close()
fh_out.close()



