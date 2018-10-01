import string

def trans(test_case):
  trans_table = string.maketrans(string.ascii_lowercase, "yhesocvxduiglbkrztnwjpfmaq")
  decrypted_text = test_case.translate(trans_table)
  return decrypted_text

def process_tests(command_to_run):
    in_file = open('in')
    out_file = open("out","w")
    number_of_tests = int(in_file.readline())
    for test_case in range(number_of_tests):
        test_string = in_file.readline()[:-1]
        test_answer = command_to_run(test_string)
        out_file.write("Case #" + str(test_case + 1) + ": " + str(test_answer) + "\n")
    out_file.close()
    in_file.close()

process_tests(trans)
