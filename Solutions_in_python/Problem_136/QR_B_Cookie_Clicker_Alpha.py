#!/usr/bin/python
# -*- coding: utf-8 -*-


class GoogleCodeJam():
    def __init__(self):
        self.file_out = None
        self.data = None

        self.input_data()

    def input_data(self):
        file_in = open(raw_input('Input Filename: '))
        self.file_out = open('result.out', 'w+')

        self.data = file_in.readlines()
        self.data.reverse()
        file_in.close()

    def pop_data(self, do_split=False):
        if do_split:
            return self.data.pop().replace('\n', '').split(' ')
        else:
            return self.data.pop().replace('\n', '')


class QRBCookieClickerAlpha(GoogleCodeJam):
    def run(self):
        t = int(self.pop_data())

        for i in xrange(0, t):
            c, f, x = self.pop_data(True)
            farm_cost = float(c)
            farm_cookie_regen = float(f)
            goal = float(x)

            time_a = 0.0
            cookie_regen = 2.0
            time_cost = 0.0

            while True:
                time_a = time_cost + goal / cookie_regen
                time_b = time_cost + farm_cost / cookie_regen + goal / (cookie_regen + farm_cookie_regen)

                if time_a <= time_b:
                    break
                else:
                    time_cost += farm_cost / cookie_regen
                    cookie_regen += farm_cookie_regen

            self.file_out.write('Case #%i: %.7f\r\n' % (i + 1, time_a))

        self.file_out.close()

if __name__ == '__main__':
    QRBCookieClickerAlpha().run()
