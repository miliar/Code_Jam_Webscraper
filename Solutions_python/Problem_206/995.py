from __future__ import print_function


class Case:
    def __init__(self, d, n, enemies, case_num):
        self.case_num = case_num
        self.d = d
        self.n = n
        self.enemies = enemies
        self._debug = True


    def calculate(self):
        biggest_time = self._time(self.enemies[0])
        for enemy in self.enemies:
            time = self._time(enemy)
            if time > biggest_time:
                biggest_time = time

        result_str = 'Case #' + str(self.case_num) + ': ' + str(float(self.d)/biggest_time)+ '\n'
        if self._debug:
            print(result_str)
        return result_str


    def _time(self, enemy):
        return (float(self.d - enemy[0]))/enemy[1]



