class HorseCruise:
    def cruise(self, case):
        spec = case[0]
        destination = int(spec[0])
        num_horses = int(spec[1])

        max_hours = 0.0000001
        for i in range(1, num_horses + 1):
            time = self.cal_time(destination, case[i])
            max_hours = max(max_hours, time)

        print('max_hours = ', max_hours)
        annie_speed = destination / max_hours
        print('annie_speed = ', annie_speed)
        return annie_speed

    def cal_time(self, destination, horse_case):
        start = int(horse_case[0])
        speed = int(horse_case[1])

        time = (destination - start) / speed
        return time
