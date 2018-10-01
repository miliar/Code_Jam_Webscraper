import sys

def read_integers(source):
    return map(int, source.split())

def file_fix_it(input_file, output_file):
    existing_count, new_count = read_integers(input_file.readline())
    existing_dirs = []
    for i in range(existing_count):
        existing_dirs.append(input_file.readline().strip())
    mkdir_count = 0
    for i in range(new_count):
        new_dir = input_file.readline().strip()
        new_path = new_dir.split('/')
        for position in range(1, len(new_path)):
            parent_path = new_path[:position+1]
            parent_dir = '/'.join(parent_path)
            if parent_dir not in existing_dirs:
                mkdir_count += 1
                existing_dirs.append(parent_dir)
    output_file.write('%d\n' % mkdir_count)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit(1)

    input_file  = open(sys.argv[1], 'r')
    output_file = open(sys.argv[2], 'w')

    case_count = int(input_file.readline())
    for case in range(1, case_count + 1):
        output_file.write('Case #%d: ' % case)
        file_fix_it(input_file, output_file)

    input_file.close()
    output_file.close()
