

def cookie_clicker_alpha(C, F, X):
    # two options
    # wait and get cookies with current rate
    # buy another farm
    t, rate, cookies = 0, 2, 0
    while cookies < X:
        wait = ((X-cookies) / rate, 1, rate)
        buy = ((C/rate) + X/(rate+F), 2, rate+F)
        action = min([wait, buy], key=lambda x:x[0])[1]
        if action == 1:
            t += (X/rate)
            cookies = t * rate
        else:
            t += (C/rate)
            rate += F
    return t

def main():
    t = int(raw_input())
    for i in range(1, t+1):
        C, F, X = (float(x) for x in raw_input().split())
        print('Case #{}: {}'.format(i, cookie_clicker_alpha(C, F,X)))

if __name__ == '__main__':
    main();

