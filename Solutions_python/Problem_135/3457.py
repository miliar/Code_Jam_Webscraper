#!/usr/bin/env python3
import sys
import os
import logging


class MagicTrick:
    def _read_question(self, file_handle, n_rows=4):
        # read the questions
        question = []
        for q in range(0, n_rows):
            question.append(set(file_handle.readline().rstrip().split()))
        return question

    def _resolve(self, ans1, q1, ans2, q2):
        row1 = q1[ans1 - 1]
        row2 = q2[ans2 - 1]

        intersect = list(row1.intersection(row2))
        logging.info("interset: %s, row1: %s, row2: %s" % (intersect, row1, row2))

        n_intersect = len(intersect)
        if n_intersect == 0:
            raise ValueError("Volunteer cheated!")
        elif n_intersect > 1:
            raise ValueError("Bad magician!")
        else:
            return intersect[0]

    def run(self, filename):
        if not os.path.exists(filename):
            raise IOError("file does not exists")

        with open(filename) as f:
            n_test_case = int(f.readline().rstrip())

            for x in range(0, n_test_case):
                ans1 = int(f.readline().rstrip())
                logging.debug("ans1: %s" % ans1)

                q1 = self._read_question(f)

                logging.debug("q1: %s " % q1)

                ans2 = int(f.readline().rstrip())

                logging.debug("ans2: %s" % ans2)

                q2 = self._read_question(f)

                logging.debug("q2: %s " % q2)

                try:
                    output = self._resolve(ans1, q1, ans2, q2)
                    print("Case #%d: %s" % (x + 1, output))
                except ValueError as e:
                    print("Case #%d: %s" % (x + 1, e))

                logging.info("-----")


logging.basicConfig(level=logging.WARN)
if len(sys.argv) <= 1:
    exit("Usage: python magictrick.py [filename]")

mt = MagicTrick()
mt.run(sys.argv[1])