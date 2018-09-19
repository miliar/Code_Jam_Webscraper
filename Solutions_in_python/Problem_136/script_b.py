__author__ = 'anoop'

import numpy as np

INPUT_FILE = 'B-large.in'
OUTPUT_FILE = 'B-large.out'



def main():
    f = open(INPUT_FILE)
    f_out = open(OUTPUT_FILE, "w")
    num_of_samples = int(f.readline()[:-1])
    for sample in range(num_of_samples):


        cookies_produced_per_second = np.float(2.0)
        line  = f.readline()[:-1]
        time = 0
        cookies = 0
        [C_needed_to_buy, F_cookies_per_second, X_target] = map(np.float, line.split(' '))
        while(1):
            time_remaining_without_buying = X_target/cookies_produced_per_second;

            time_to_buy = C_needed_to_buy / cookies_produced_per_second;
            cookies_per_second_after_buying = F_cookies_per_second + cookies_produced_per_second

            time_remaining_with_buying = X_target/cookies_per_second_after_buying + time_to_buy;

            if(time_remaining_without_buying < time_remaining_with_buying):
                time = time + time_remaining_without_buying
                cookies = cookies + cookies_produced_per_second * time;
            else:
                time = time + time_to_buy
                cookies = cookies + cookies_produced_per_second * time_to_buy
                cookies_produced_per_second = F_cookies_per_second + cookies_produced_per_second

            if cookies >= X_target:
                write_sample = sample + 1
                f_out.write('Case #%d: %.7f\n'%(write_sample, time))
                break

    f.close()
    f_out.close()

if __name__ == "__main__":
    main()
