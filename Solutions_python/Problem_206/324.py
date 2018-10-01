import numpy as np

if __name__ == '__main__':
    t = int(raw_input())

    for t_i in np.arange(t):
        d, n = raw_input().split(" ")
        d = int(d) # destination
        n = int(n) # number horses

        time_list = []
        for n_i in np.arange(n):
            k, s = raw_input().split(" ")
            k = int(k) # start pos
            s = int(s) # speed

            if k < d:
                t = float(d-k)/float(s)
                time_list.append(t)

        s_annie = float(d)/float(np.max(time_list))

        print 'Case #%d: ' % (t_i + 1) + str(s_annie)