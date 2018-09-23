import sys

arg_list = sys.argv
input_file = open(arg_list[1], 'r')
ouput_file = open(arg_list[2], 'w')
contents = input_file.read()
contents_list = contents.split('\n')

T = int(contents_list[0])
for N in contents_list[1:T+1]:
  for y in range(1, int(N)+1):
    if str(y) == ''.join(sorted(str(y))):
      last_tidy = y
  ouput_file.write("Case #{}: {}\n".format(contents_list.index(N), last_tidy))

ouput_file.close()
input_file.close()
