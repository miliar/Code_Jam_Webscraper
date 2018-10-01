if __name__ == "__main__":

    with open("sample.txt", "r") as f:
        test_c = int(f.readline())

        for t in range(1, test_c + 1):


            first_row_idx = int(f.readline())
            first_arr = None

            for i in range(1, 5):
                if i == first_row_idx:
                    first_arr = [int(v) for v in f.readline().split(" ")]
                else:
                    f.readline()

            second_row_idx = int(f.readline())
            second_arr = None

            for i in range(1, 5):
                if i == second_row_idx:
                    second_arr = [int(v) for v in f.readline().split(" ")]
                else:
                    f.readline()

            common = [e for e in first_arr if e in second_arr]
            common_len = len(common)

            if common_len == 1:
                print "Case #" + str(t) + ": " + str(common[0])
            elif common_len > 1:
                print "Case #" + str(t) + ": Bad magician!"
            else:
                print "Case #" + str(t) + ": Volunteer cheated!"