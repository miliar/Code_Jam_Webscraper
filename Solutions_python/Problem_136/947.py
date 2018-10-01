
def time_to_get_cookies(gain, X):
    return X / gain


def time_to_get_cookies_with_fact(gain, X, C, F):
    return (C/gain) + ( ( X ) / ( gain + F ) )


def solve(C, F, X):
    cookie_gain = 2.0
    time_count = 0.0

    while time_to_get_cookies(cookie_gain, X) > time_to_get_cookies_with_fact(cookie_gain, X, C, F):
#        print('----------- ' + str(cookie_gain))
#        print(time_to_get_cookies(cookie_gain, X))
#        print(time_to_get_cookies_with_fact(cookie_gain, X, C, F))
        time_count += (C / cookie_gain)
        cookie_gain += F

    return time_count + time_to_get_cookies(cookie_gain, X)


#with open('sample.in') as f:
with open('B-large.in') as f:
    T = int(f.readline())

    for puzzle_count in range(T):
        C, F, X = map(float, f.readline().split(' '))

        ans = solve(C,F,X)
        print('Case #%s: %s'%(str(puzzle_count + 1), str(ans)))


